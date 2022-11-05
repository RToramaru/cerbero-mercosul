<?php

namespace app\models;

use Yii;

/**
 * This is the model class for table "veiculo".
 *
 * @property int $id Identificador do veículo
 * @property string $placa Placa do veículo
 * @property string $data Data de cadastro do veículo
 * @property string $imagem Imagem do veículo
 */
class Veiculo extends \yii\db\ActiveRecord
{
    /**
     * {@inheritdoc}
     */
    public static function tableName()
    {
        return 'veiculo';
    }

    /**
     * {@inheritdoc}
     */
    public function rules()
    {
        return [
            [['placa', 'data', 'imagem'], 'required', 'message' => 'Campo obrigatório'],
            [['placa', 'imagem'], 'string'],
            [['data'], 'safe'],
        ];
    }

    /**
     * {@inheritdoc}
     */
    public function attributeLabels()
    {
        return [
            'id' => 'ID',
            'placa' => 'Placa',
            'data' => 'Data',
            'imagem' => 'Imagem',
        ];
    }
}
